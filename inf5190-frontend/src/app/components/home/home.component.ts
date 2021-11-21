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
  glissades_details: Glissade = null as any;
  glissadesNbr: number = 0;
  patinoires: Patinoire[] = [];
  patinoire_details: Patinoire = null as any;
  patinoire_nbr: number = 0;
  inst_names: string[] = []
  condition_years:  Set<number> = new Set<number>();
  results: number = 0;
  searchResult: boolean = true;
  selectedPatinoir: boolean = false;
  conditionsOfSelectedYear: PatinoirCondition[] = []
  condsNbrPerPat : number = 0;
  instAquaNbr: number = 0;

  searchForm: FormGroup;
  instAquaForm: FormGroup;
  glissadeForm: FormGroup;
  patinoireForm: FormGroup;
  yearsForm: FormGroup


  constructor(private apiClient: ApiClientService, private formBuilder: FormBuilder) {
    this.searchForm = this.formBuilder.group({
      search: ['', Validators.required]
    })
    this.instAquaForm = this.formBuilder.group({
      aquaInstaName: ['', Validators.required]
    })
    this.glissadeForm = this.formBuilder.group({
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
    this.searchResult = true;
    this.arr_name = this.searchForm.value;
    console.log('Search key word : ',this.searchForm.value)
    this.apiClient.getInstallationsPerArrondissement(this.searchForm.value)
                  .subscribe((installations: Installation)=>{
      this.arr_cle = installations.arr_cle;
      this.aqua_inst = installations.aqua_inst;
      this.aqua_inst_nbr = this.aqua_inst.length;
      this.glissades = installations.glissades;
      this.glissadesNbr = this.glissades.length;
      this.patinoires = installations.patinoires;
      this.patinoire_nbr = this.patinoires.length;
      this.searchForm.reset()
    },
    (error: HttpErrorResponse)=>{
      this.ReInitialize();
      this.searchResult = false;
      this.errorMessage = error.error.message;
      console.log('error status:', error.status);
      console.log('error message :', error.message);
      console.log('error statusText :',error.statusText);
    })
  }


  public getAquaInstallationDetails(): void{
    const aquaName = this.instAquaForm.value['aquaInstaName']
    console.log('Choosen aqua inst name :',aquaName)
    this.apiClient.getAquaInstallationDetails(this.arr_name, aquaName)
                  .subscribe((aquaInst: InstallationAquatique[])=>{
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
    this.apiClient.getPatinoireDetails(this.arr_name, patName)
                  .subscribe((response: Patinoire)=>{
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


  public getGlissadeDetails(): void{
    const name = this.glissadeForm.value['glissadeName']
    console.log('Choosen glissade name :',name)
    this.apiClient.getGlissadeDetails(this.arr_name, name)
                  .subscribe((response : Glissade)=>{
      this.glissades_details = response;
      this.glissadesNbr = 1;

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
    this.glissadesNbr = 0;
    this.aqua_inst_details = []
    this.glissades_details =  null as any;
    this.patinoire_details = null as any;
    this.selectedPatinoir = false
    this.aqua_inst = [];
    this.glissades = [];
    this.patinoires = []
    this.conditionsOfSelectedYear = []
  }

}
