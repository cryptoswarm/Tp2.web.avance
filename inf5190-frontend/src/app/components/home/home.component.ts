import { EditAquaComponent } from './../edit-aqua/edit-aqua.component';
import { GlissadeServiceService } from 'src/app/services/glissade-service.service';
import { AquaInstService } from 'src/app/services/aqua-inst.service';
import { ComponentRef, Type } from '@angular/core';
import { PatinoirCondition } from './../../models/patinoire-conditions';
import { Installation } from './../../models/installation';
import { Component, OnInit } from '@angular/core';
import { ApiClientService } from 'src/app/services/api-client.service';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { InstallationAquatique } from 'src/app/models/installation-aquatique';
import { Glissade } from 'src/app/models/glissade';
import { Patinoire } from 'src/app/models/patinoire';
import { DeletionComponent } from '../deletion/deletion.component';
import { EditGlissadeComponent } from '../edit-glissade/edit-glissade.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';


const MODALS: { [name: string]: Type<any> } = {
  autofocus: DeletionComponent,
  glissade: EditGlissadeComponent,
  aquaInst: EditAquaComponent
};

@Component({
  selector: 'app-home',
  // directives: [EditGlissadeComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  installations: Installation = null as any;

  errorMessage: string = "";
  updateSuccess: boolean = false;

  arr_name: string = "";
  arr_cle!: string;
  aqua_inst: InstallationAquatique[] = [];
  aqua_inst_details: InstallationAquatique[] = [];
  aqua_inst_nbr: number = 0;
  glissades: Glissade[] = [];
  glissadeDetails: Glissade = null as any;
  glissadesNbr: number = 0;
  patinoires: Patinoire[] = [];
  patinoire_details: Patinoire = null as any;
  patinoire_nbr: number = 0;
  condition_years:  Set<number> = new Set<number>();
  searchResult: boolean = true;
  selectedPatinoir: boolean = false;
  conditionsOfSelectedYear: PatinoirCondition[] = []

  searchForm: FormGroup;
  instAquaForm: FormGroup;
  glissadeForm: FormGroup;
  patinoireForm: FormGroup;
  yearsForm: FormGroup

  constructor(private apiClient: ApiClientService,
              private _sharedService :SharedServiceService,
              private formBuilder: FormBuilder,
              private _modalService: NgbModal,
              private _glissadeService: GlissadeServiceService,
              private _aquaInstallationService: AquaInstService) {
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

  ngOnInit(): void {
  }


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
    this.updateSuccess = false;
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
    this.updateSuccess = false;
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
    this.updateSuccess = false;
    const name = this.glissadeForm.value['glissadeName']
    console.log('Glissade name update/delete:',name)
    this.apiClient.getGlissadeDetails(this.arr_name, name)
                  .subscribe((response : Glissade)=>{
      this.glissadeDetails = response;
      console.log('Glissade details update/delete: ',this.glissadeDetails)
      this.glissadesNbr = 1;

    },
    (error: HttpErrorResponse)=>{
      this.glissadesNbr = 0;
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
    this.glissadeDetails =  null as any;
    this.patinoire_details = null as any;
    this.selectedPatinoir = false
    this.aqua_inst = [];
    this.glissades = [];
    this.patinoires = []
    this.conditionsOfSelectedYear = []
  }

  public deleteAquaInstallation(aquaInstId: number| undefined): void {

  }

  public editAquaInstallation(aqua_inst: InstallationAquatique){
    console.log('aqua_inst data in home compo update method:', aqua_inst)
    this.updateSuccess = false;
    if(aqua_inst !== undefined){
      this._sharedService.aquaInstallation = aqua_inst;
      this.open('aquaInst');
      this._aquaInstallationService.refreshNeeded$
          .subscribe(()=>{
              this.getAquaInstallationDetails();
              this.updateSuccess = true;
          })
    }
  }

  public editGlissade(glissade: Glissade | undefined): void {
    console.log('edit button pressed')
    this.updateSuccess = false;
    if(glissade !== undefined){
      this._sharedService.glissade = glissade;
      this.open('glissade');
      this._glissadeService.refreshNeeded$
          .subscribe(()=>{
          this.getGlissadeDetails();
          this.updateSuccess = true;
      })
      console.log('Glissade id to be updated:',glissade.id)
    }
  }

  public deleteInstallation(id: number | undefined, type: string, name: string| undefined): void {
    console.log('delete button pressed')
    if(id !== undefined && type != undefined && name!= undefined){
      this._sharedService.installationId = id;
      this._sharedService.installationType = type;
      this._sharedService.installationName = name;
      this.open('autofocus');
      this._aquaInstallationService.deleteNotifier$
          .subscribe(()=>{
          if(type == 'glissade'){
            this.deleteHelper(this.glissades, id);
            this.glissadeDetails = null as any;
            this.glissadesNbr = 0;
          }else if(type == 'installation-aquatique'){
            this.deleteHelper(this.aqua_inst, id);
            this.aqua_inst_details = null as any;
            this.aqua_inst_nbr = 0;
          }else if(type == 'patinoire-condition'){
            this.deleteHelper(this.conditionsOfSelectedYear, id);
            this.patinoire_nbr = this.patinoire_nbr > 1 ? this.patinoire_nbr -1 : 0;
          }
      })
      console.log('Installation id to be deleted :',id)
    }
  }


  open(name: string) {
    this._modalService.open(MODALS[name]);
  }

  private deleteHelper(inst: Glissade[] | InstallationAquatique[] | PatinoirCondition[], id: number): void{
    const index = inst.findIndex(inst => inst.id == id);
    inst.splice(index, 1);
  }


}
