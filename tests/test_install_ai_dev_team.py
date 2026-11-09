"""Behavioral tests for the safe AI DEV TEAM installer."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


INSTALLER = Path(__file__).resolve().parents[1] / "scripts" / "install_ai_dev_team.py"


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.target = self.root / "target"
        (self.source / ".agents" / "agents").mkdir(parents=True)
        self.target.mkdir()
        (self.source / "AGENTS.md").write_text("# canonical rules\n", encoding="utf-8")
        (self.source / ".agents" / "agents" / "director.md").write_text(
            "# Director\n", encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def run_installer(self, *extra):
        return subprocess.run(
            [
                sys.executable,
                str(INSTALLER),
                "--source",
                str(self.source),
                "--target",
                str(self.target),
                *extra,
            ],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_dry_run_does_not_write(self):
        result = self.run_installer("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.target / "AGENTS.md").exists())
        self.assertIn("DRY RUN", result.stdout)

    def test_installs_core_files(self):
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (self.target / "AGENTS.md").read_text(encoding="utf-8"),
            "# canonical rules\n",
        )
        self.assertTrue((self.target / ".agents" / "agents" / "director.md").is_file())

    def test_conflict_aborts_without_partial_copy(self):
        (self.target / "AGENTS.md").write_text("# local rules\n", encoding="utf-8")
        result = self.run_installer()
        self.assertEqual(result.returncode, 3)
        self.assertFalse((self.target / ".agents").exists())
        self.assertEqual(
            (self.target / "AGENTS.md").read_text(encoding="utf-8"),
            "# local rules\n",
        )

    def test_skip_conflicts_preserves_existing_and_copies_missing(self):
        (self.target / "AGENTS.md").write_text("# local rules\n", encoding="utf-8")
        result = self.run_installer("--skip-conflicts")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (self.target / "AGENTS.md").read_text(encoding="utf-8"),
            "# local rules\n",
        )
        self.assertTrue((self.target / ".agents" / "agents" / "director.md").is_file())

    def test_identical_files_are_skipped(self):
        (self.target / "AGENTS.md").write_text("# canonical rules\n", encoding="utf-8")
        result = self.run_installer()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SKIP  1 identical file(s)", result.stdout)


if __name__ == "__main__":
    unittest.main()
