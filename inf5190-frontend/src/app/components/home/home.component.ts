import { Installation } from './../../models/installation';
import { Component, OnInit } from '@angular/core';
import { ApiClientService } from 'src/app/services/api-client.service';
import { HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { InstallationAquatique } from 'src/app/models/installation-aquatique';
import { Glissade } from 'src/app/models/glissade';
import { Patinoire } from 'src/app/models/patinoire';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  installations: Installation = null as any;

  errorMessage: string = "";

  arr_name!: string;
  arr_cle!: string;
  aqua_inst: InstallationAquatique[] = []
  glissades: Glissade[] = [];
  patinoires: Patinoire[] = [];
  inst_names: string[] = []
  results: number = 0;

  searchForm: FormGroup;


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
  }

  ngOnInit(): void {
    this.getAllInstallations()
  }

  public getAllInstallations(){
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value).subscribe((installations: Installation)=>{
      // this.installations = installations


      this.arr_name = installations.arr_name;
      this.arr_cle = installations.arr_cle;
      this.aqua_inst = installations.aqua_inst;
      this.inst_names = this.getInstallationName(installations.aqua_inst);
      this.results = installations.aqua_inst.length;
      this.searchForm.reset()
    },
    (error: HttpErrorResponse)=>{
      this.errorMessage = error.error.message;
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText)
    })
  }

  public getInstallationName(installations: InstallationAquatique[]): string[]{
    let inst_names: string[] = []
    installations.forEach(element => {
      inst_names.push(element.nom_installation)
    });
    return inst_names;
  }

}
