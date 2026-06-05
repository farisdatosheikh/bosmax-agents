import { spawnSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

function fail(message: string): never {
	console.error(`MANDOR FAIL: ${message}`);
	process.exit(1);
}

function runPythonValidator(args: string[]): void {
	const result = spawnSync("python", args, {
		cwd: ROOT,
		encoding: "utf-8",
		stdio: "inherit",
	});
	if (result.status !== 0) {
		fail(`Validator failed: python ${args.join(" ")}`);
	}
}

const ROOT = resolve(__dirname, "..");
const moduleStatusPath = resolve(ROOT, "docs", "MODULE_STATUS.yaml");

if (!existsSync(moduleStatusPath)) {
	fail("docs/MODULE_STATUS.yaml missing");
}

const moduleStatusText = readFileSync(moduleStatusPath, "utf-8");
if (!moduleStatusText.includes("resolver_runtime:")) {
	fail("resolver_runtime domain missing from docs/MODULE_STATUS.yaml");
}
if (!moduleStatusText.includes("status: IN_PROGRESS")) {
	fail("resolver_runtime must remain IN_PROGRESS in docs/MODULE_STATUS.yaml");
}

const requiredFiles = [
	"BOSMAX_COPYWRITING_ID_RESOLVER_v1.xlsx",
	"BOSMAX_AVATAR_CONTEXT_RESOLVER_v1.xlsx",
	"registries/copywriting_id_resolver.yaml",
	"registries/avatar_context_rotation.yaml",
	"docs/notion_resolver_database_handoff_v1.md",
	"docs/notion_bosmax_command_centre_template_v1.md",
];

for (const relativePath of requiredFiles) {
	if (!existsSync(resolve(ROOT, relativePath))) {
		fail(`Required resolver artifact missing: ${relativePath}`);
	}
}

runPythonValidator(["scripts/validate_copywriting_id_resolver.py"]);
runPythonValidator(["scripts/validate_avatar_context_resolver.py"]);
runPythonValidator(["scripts/validate_product_on_the_fly_video_prompt.py"]);

console.log("MANDOR CHECK PASSED: resolver_runtime");
