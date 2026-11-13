from pathlib import Path
from tempfile import TemporaryDirectory
from django.test import SimpleTestCase, override_settings


class DownloadTests(SimpleTestCase):
    def test_download_pdf(self):
        with TemporaryDirectory() as tmp:
            folder = Path(tmp) / "files"
            folder.mkdir()
            (folder / "sample.pdf").write_bytes(b"%PDF-1.4\n%test\n")
            with override_settings(BASE_DIR=Path(tmp)):
                response = self.client.get("/download/")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response["Content-Type"], "application/pdf")
                self.assertIn("attachment", response["Content-Disposition"])
                response.close()
