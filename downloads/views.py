from pathlib import Path
from django.conf import settings
from django.http import FileResponse, Http404


def download_pdf(request):
    file_path = Path(settings.BASE_DIR) / "files" / "setup.exe"
    if not file_path.is_file():
        raise Http404("PDF not found")
    response = FileResponse(file_path.open("rb"), as_attachment=True,
                        filename="setup.exe", content_type="application/pdf")
    
    response["X-Content-Type-Options"] = "nosniff"
    response["Cache-Control"] = "no-store"
    
    
    return response
