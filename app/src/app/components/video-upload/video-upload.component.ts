import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-video-upload',
  templateUrl: './video-upload.component.html',
  styleUrls: ['./video-upload.component.css']
})
export class VideoUploadComponent implements OnInit {

  fileToUpload: File = null;
  fileUploadService: any;
  httpClient: HttpClient;

  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  uploadFileToActivity() {
    this.fileUploadService.postFile(this.fileToUpload).subscribe(data => {
      // do something, if upload success
      }, error => {
        console.log(error);
      });
  }
  
  postFile(fileToUpload: File): Observable<Boolean> {
    const endpoint = 'your-destination-url';
    const formData: FormData = new FormData();
    const yourHeadersConfig = {"content-type": "application/octet-stream"}
    formData.append('fileKey', fileToUpload, fileToUpload.name);
    var resp = this.httpClient
      .post(endpoint, formData, { headers: yourHeadersConfig });
    return;
}
  constructor() { }

  ngOnInit(): void {
  }

}
