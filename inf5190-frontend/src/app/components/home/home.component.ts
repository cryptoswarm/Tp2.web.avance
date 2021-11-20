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
  patinoires_perm: Patinoire[] = [];
  inst_names: string[] = []
  glissade_names : string[] = []
  patinoires_names : string[] = []
  condition_years:  Set<number> = new Set<number>();
  results: number = 0;
  searchResult: boolean = false;
  selectedPatinoir: Patinoire = null as any;
  conditionsOfSelectedYear: PatinoirCondition[] = []
  condsNbrPerPat : number = 0;
  instAquaNbr: number = 0;

  searchForm: FormGroup;
  instNamesForm: FormGroup;
  glissadeNamesForm: FormGroup;
  patinoireNamesForm: FormGroup;
  yearsForm: FormGroup


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
    this.instNamesForm = this.formBuilder.group({
      aquaInstaName: ['', Validators.required]
    })
    this.glissadeNamesForm = this.formBuilder.group({
      glissadeName: ['', Validators.required]
    })
    this.patinoireNamesForm = this.formBuilder.group({
      patinoireName: ['', Validators.required]
    })
    this.yearsForm = this.formBuilder.group({
      conditionyear: ['', Validators.required]
    })
  }

  ngOnInit(): void {}


  public getAllInstallations(){
    this.arr_name = this.searchForm.value;
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value).subscribe((installations: Installation)=>{
      this.searchResult = false;
      this.arr_cle = installations.arr_cle;
      this.aqua_inst = installations.aqua_inst;
      console.log('this.aqua_inst :',this.aqua_inst)
      this.aqua_inst_nbr = this.aqua_inst.length
      this.glissades = installations.glissades
      console.log('this.glissades :',this.glissades)
      this.patinoires = installations.patinoires
      console.log('this.patinoires :',this.patinoires)
      this.searchForm.reset()
    },
    (error: HttpErrorResponse)=>{
      this.searchResult = true;
      this.aqua_inst = [];
      this.inst_names = [];
      this.conditionsOfSelectedYear = [];
      this.results = 0;
      this.selectedPatinoir = null as any;
      this.errorMessage = error.error.message;
      this.condition_years.clear();
      this.patinoires_perm = [];
      this.glissades_perm = []
      this.condsNbrPerPat  = 0;
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText)
    })
  }


  public getAquaInstallationDetails(): void{
    // alert(JSON.stringify(this.instNamesForm.value))
    const aquaName = this.instNamesForm.value['aquaInstaName']
    console.log('Choosen aqua inst name :',aquaName)
    this.apiClient.getAquaInstallationDetails(this.arr_name, aquaName).subscribe((aquaInst: InstallationAquatique[])=>{
        this.aqua_inst_details = aquaInst;
        this.aqua_inst_nbr = aquaInst.length
        console.log(this.aqua_inst_details)
    })
  }



  public getAquaInstallationName(installations: InstallationAquatique[]): string[]{
    let inst_names: string[] = []
    installations.forEach(element => {
      inst_names.push(element.nom_installation)
    });
    return inst_names;
  }

  public getGlissadesNames(installations: Glissade[]): string[]{
    let glissades_names: string[] = []
    installations.forEach(element => {
      glissades_names.push(element.name)
    });
    return glissades_names;
  }

  public getPatinoiresNames(installations: Patinoire[]): string[]{
    let patinoires_names: string[] = []
    installations.forEach(element => {
      patinoires_names.push(element.nom_pat)
      // element?.conditions.forEach(condition => {
      //   let year:number  = new Date(condition.date_heure).getFullYear();
      //   this.condition_years.add(year);
      // });
    });
    return patinoires_names;
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



  public filterByGlissadeName(): void{
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
    const name = this.patinoireNamesForm.value['patinoireName']
    console.log('Choosen patinoire name :',name)
    let result :Patinoire = null as any;
    this.patinoires_perm.forEach(element => {
      console.log('element.name patinoire: ',element.nom_pat);
      if(element.nom_pat.indexOf(name) !== -1){
        result = element;
        console.log('filtering by :'+name+' gives :', result)
      }
    });
    this.selectedPatinoir = result;
    // this.condsNbrPerPat = this.selectedPatinoir?.conditions.length;
  }

  public filterByYear(): void {
    // const selectedYear = this.yearsForm.value['conditionyear']
    // console.log('selected year : ',selectedYear)
    // this.conditionsOfSelectedYear = this.selectedPatinoir
    //                                 ?.conditions
    //                                 .filter(condition =>
    //                                 new Date(condition.date_heure).getFullYear() == selectedYear);

    // this.condsNbrPerPat  = this.conditionsOfSelectedYear.length;

  }

}
