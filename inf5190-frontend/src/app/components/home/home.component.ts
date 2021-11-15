import { Installation } from './../../models/installation';
import { Component, OnInit } from '@angular/core';
import { ApiClientService } from 'src/app/services/api-client.service';
import { HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  installations: Installation[]= []
  errorMessage: string = "";
  searchForm: FormGroup;


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
  }

  ngOnInit(): void {
  }

  public getAllInstallations(){
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value).subscribe((installations: Installation[])=>{
      this.installations = installations
      console.log(installations)
    },
    (error: HttpErrorResponse)=>{
      this.errorMessage = error.error.message;
      console.log('error.error.status:', error.error.status);
      console.log('error.error.message :', error.error.message);
      console.log('error.message :', error.message);
    })
  }

}
