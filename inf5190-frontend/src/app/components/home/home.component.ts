import { PatinoirCondition } from './../../models/patinoire-conditions';
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

  arr_name: string = "";
  arr_cle!: string;
  aqua_inst: InstallationAquatique[] = [];
  aqua_inst_details: InstallationAquatique[] = [];
  aqua_inst_nbr: number = 0;
  glissades: Glissade[] = [];
  glissades_perm: Glissade[] = [];
  patinoires: Patinoire[] = [];
  patinoire_details: Patinoire = null as any;
  patinoire_nbr: number = 0;
  inst_names: string[] = []
  glissade_names : string[] = []
  patinoires_names : string[] = []
  condition_years:  Set<number> = new Set<number>();
  results: number = 0;
  searchResult: boolean = false;
  selectedPatinoir: boolean = false;
  conditionsOfSelectedYear: PatinoirCondition[] = []
  condsNbrPerPat : number = 0;
  instAquaNbr: number = 0;

  searchForm: FormGroup;
  instAquaForm: FormGroup;
  glissadeNamesForm: FormGroup;
  patinoireForm: FormGroup;
  yearsForm: FormGroup


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
    this.instAquaForm = this.formBuilder.group({
      aquaInstaName: ['', Validators.required]
    })
    this.glissadeNamesForm = this.formBuilder.group({
      glissadeName: ['', Validators.required]
    })
    this.patinoireForm = this.formBuilder.group({
      patinoireName: ['', Validators.required]
    })
    this.yearsForm = this.formBuilder.group({
      conditionyear: ['', Validators.required]
    })
  }

  ngOnInit(): void {}


  public getAllInstallations(){
    this.ReInitialize()
    this.arr_name = this.searchForm.value;
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value)
                  .subscribe((installations: Installation)=>{
      this.searchResult = false;
      this.arr_cle = installations.arr_cle;
      this.aqua_inst = installations.aqua_inst;
      this.aqua_inst_nbr = this.aqua_inst.length
      this.glissades = installations.glissades
      this.patinoires = installations.patinoires
      this.patinoire_nbr = this.patinoires.length;
      this.searchForm.reset()
    },
    (error: HttpErrorResponse)=>{
      this.ReInitialize()
      this.errorMessage = error.error.message;
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText)
    })
  }


  public getAquaInstallationDetails(): void{
    const aquaName = this.instAquaForm.value['aquaInstaName']
    console.log('Choosen aqua inst name :',aquaName)
    this.apiClient.getAquaInstallationDetails(this.arr_name, aquaName).subscribe((aquaInst: InstallationAquatique[])=>{
        this.aqua_inst_details = aquaInst;
        this.aqua_inst_nbr = aquaInst.length
        console.log(this.aqua_inst_details)
    },
    (error: HttpErrorResponse)=>{
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText)
    })
  }

  public getPatinoiresDetails(): void{
    const patName = this.patinoireForm.value['patinoireName']
    console.log('Choosen patinoire name :',patName)
    this.apiClient.getPatinoireDetails(this.arr_name, patName).subscribe((response: Patinoire)=>{
        this.patinoire_details = response;
        this.patinoire_nbr = 1;
        this.selectedPatinoir = true;
        this.getAllYears(this.patinoire_details)
        this.conditionsOfSelectedYear = []
    },
    (error: HttpErrorResponse)=>{
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText)
    })
  }

  public getAllYears(patinoire: Patinoire): void {
      patinoire.conditions?.forEach(condition => {
        let year: number  = new Date(condition.date_heure).getFullYear();
        this.condition_years.add(year);
      });
  }

  public filterByYear(): void {
    this.conditionsOfSelectedYear = []
    let selectedYear: number = this.yearsForm.value['conditionyear']
    console.log('selected year : ',selectedYear)
    this.patinoire_details.conditions?.forEach(condition => {
      if(new Date(condition.date_heure).getFullYear() == selectedYear){
        this.conditionsOfSelectedYear.push(condition)
      }
    })
    this.patinoire_nbr  = this.conditionsOfSelectedYear.length;
  }

  public ReInitialize(): void {
    this.aqua_inst_nbr = 0;
    this.patinoire_nbr = 0;
    this.aqua_inst_details = []
    this.selectedPatinoir = false
    this.aqua_inst = [];
    this.glissades = [];
    this.patinoires = []
    this.conditionsOfSelectedYear = []
  }

  // public getAquaInstallationName(installations: InstallationAquatique[]): string[]{
  //   let inst_names: string[] = []
  //   installations.forEach(element => {
  //     inst_names.push(element.nom_installation)
  //   });
  //   return inst_names;
  // }

  // public getGlissadesNames(installations: Glissade[]): string[]{
  //   let glissades_names: string[] = []
  //   installations.forEach(element => {
  //     glissades_names.push(element.name)
  //   });
  //   return glissades_names;
  // }

  // public getPatinoiresNames(installations: Patinoire[]): string[]{
  //   let patinoires_names: string[] = []
  //   installations.forEach(element => {
  //     patinoires_names.push(element.nom_pat)
  //     // element?.conditions.forEach(condition => {
  //     //   let year:number  = new Date(condition.date_heure).getFullYear();
  //     //   this.condition_years.add(year);
  //     // });
  //   });
  //   return patinoires_names;
  // }

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
  // public filterByInstallationName(): void{
  //   // alert(JSON.stringify(this.instNamesForm.value))
  //   const name = this.instNamesForm.value['instaName']
  //   console.log('Choosen instllation name :',name)
  //   const result :InstallationAquatique[] = [];
  //   this.aqua_inst_perm.forEach(element => {
  //     console.log('element.nom_installation: ',element.nom_installation);
  //     console.log(element.nom_installation.indexOf(name) !== -1)
  //     if(element.nom_installation.indexOf(name) !== -1){
  //       result.push(element)
  //       console.log('filtering by :'+name+' gives :', result)
  //     }
  //   });
  //   this.aqua_inst = result;
  //   this.instAquaNbr = this.aqua_inst.length;
  // }



  public getGlissadeDetails(): void{
    // alert(JSON.stringify(this.instNamesForm.value))
    const name = this.glissadeNamesForm.value['glissadeName']
    console.log('Choosen glissade name :',name)
    const result :Glissade[] = [];
    this.glissades_perm.forEach(element => {
      console.log('element.name glissade: ',element.name);
      console.log(element.name.indexOf(name) !== -1)
      if(element.name.indexOf(name) !== -1){
        result.push(element)
        console.log('filtering by :'+name+' gives :', result)
      }
    });
    this.glissades = result;
  }

  public filterByPatinoireName(): void{
    // const name = this.patinoireNamesForm.value['patinoireName']
    // console.log('Choosen patinoire name :',name)
    // let result :Patinoire = null as any;
    // this.patinoires_perm.forEach(element => {
    //   console.log('element.name patinoire: ',element.nom_pat);
    //   if(element.nom_pat.indexOf(name) !== -1){
    //     result = element;
    //     console.log('filtering by :'+name+' gives :', result)
    //   }
    // });
    // this.selectedPatinoir = result;
    // this.condsNbrPerPat = this.selectedPatinoir?.conditions.length;
  }



}
