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
  aqua_inst: InstallationAquatique[] = [];
  aqua_inst_perm: InstallationAquatique[] = [];
  glissades: Glissade[] = [];
  patinoires: Patinoire[] = [];
  inst_names: string[] = []
  results: number = 0;
  searchResult: boolean = false;

  searchForm: FormGroup;
  instNamesForm: FormGroup;


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
    this.instNamesForm = this.formBuilder.group({
      instaName: ['', Validators.required]
    })
  }

  ngOnInit(): void {
    // this.getAllInstallations()
  }

  public getAllInstallations(){
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value).subscribe((installations: Installation)=>{
      // this.installations = installations

      this.searchResult = false;
      this.arr_name = installations.arr_name;
      this.arr_cle = installations.arr_cle;
      this.aqua_inst = installations.aqua_inst;
      this.aqua_inst_perm = installations.aqua_inst;
      console.log('this.aqua_inst :',this.aqua_inst)
      this.inst_names = this.getInstallationName(installations.aqua_inst);
      this.results = installations.aqua_inst.length;
      this.searchForm.reset()
    },
    (error: HttpErrorResponse)=>{
      this.searchResult = true;
      this.aqua_inst = [];
      this.aqua_inst_perm = [];
      this.inst_names = [];
      this.results = 0;
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

  // public searchEmployees(key: string):void{
  //   console.log(key);
  //   const result : Employee[] = [] //a new array of employees
  //   for (const employee of this.employees){
  //       if(employee.name.toLowerCase().indexOf(key.toLowerCase()) !== -1
  //         || employee.email.toLowerCase().indexOf(key.toLowerCase()) !== -1
  //         || employee.jobTitle.toLowerCase().indexOf(key.toLowerCase()) !== -1
  //         || employee.phone.toLowerCase().indexOf(key.toLowerCase()) !== -1){
  //         result.push(employee);
  //       }
  //   }
  //   this.employees =  result; //employees to be shown are those that match the search key
  //   if(result.length === 0 || !key){  //if no employee match the search or the user has not enterned any key "!key"
  //     this.getEmployees();
  //   }
  // }
  public filterByInstallationName(): void{
    // alert(JSON.stringify(this.instNamesForm.value))
    const name = this.instNamesForm.value['instaName']
    console.log('Choosen instllation name :',name)
    const result :InstallationAquatique[] = [];
    this.aqua_inst_perm.forEach(element => {
      console.log('element.nom_installation: ',element.nom_installation);
      console.log(element.nom_installation.indexOf(name) !== -1)
      if(element.nom_installation.indexOf(name) !== -1){
        result.push(element)
        console.log('filtering by :'+name+' gives :', result)
      }
    });
    this.aqua_inst = result;
  }

  // public onSubmit(){
  //   //console.log('submitted')
  //   alert(JSON.stringify(this.instNamesForm.value))
  // }

}