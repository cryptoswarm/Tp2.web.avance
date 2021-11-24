import { AquaInstService } from './../../services/aqua-inst.service';
import { InstallationAquatique } from 'src/app/models/installation-aquatique';
import { Component, OnInit } from '@angular/core';
import Swal, { SweetAlertIcon } from 'sweetalert2';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { NotifierService } from 'src/app/services/notifier.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-edit-aqua',
  templateUrl: './edit-aqua.component.html',
  styleUrls: ['./edit-aqua.component.css']
})
export class EditAquaComponent implements OnInit {

  editAquaInst!: InstallationAquatique;

  errorMessage: string = "";
  errorMessages: string[] = [];
  nom_installation: string = '';
  type_installation: string= '';
  adress: string= '';
  propriete_installation: string= '';
  gestion_inst: string= '';
  equipement_inst: string= '';
  success : boolean = false;

  aquaInstForEditForm!: FormGroup;

  constructor(private _sharedService:SharedServiceService,
              private _notifierService: NotifierService,
              private _aquaService : AquaInstService,
              private _formBuilder: FormBuilder,
              public modal: NgbActiveModal) {}

  ngOnInit(): void {

    this.aquaInstForEditForm = this._formBuilder.group({
      nom_installation: ['', Validators.required],
      type_installation: ['', Validators.required],
      adress: ['', Validators.required],
      propriete_installation: ['', Validators.required],
      gestion_inst: ['', Validators.required],
      equipement_inst: ['', Validators.required]
    })

    this.editAquaInst = this._sharedService.aquaInstallation;
    if(this.editAquaInst.nom_installation !== undefined){
        this.aquaInstForEditForm.get('nom_installation')?.setValue(this.editAquaInst.nom_installation);
    }
    if(this.editAquaInst.type_installation !== undefined){
        this.aquaInstForEditForm.get('type_installation')?.setValue(this.editAquaInst.type_installation);
    }
    if(this.editAquaInst.adress !== undefined){
        this.aquaInstForEditForm.get('adress')?.setValue(this.editAquaInst.adress);
    }
    if(this.editAquaInst.propriete_installation !== undefined){
        this.aquaInstForEditForm.get('propriete_installation')?.setValue(this.editAquaInst.propriete_installation);
    }
    if(this.editAquaInst.gestion_inst !== undefined){
        this.aquaInstForEditForm.get('gestion_inst')?.setValue(this.editAquaInst.gestion_inst);
    }
    if(this.editAquaInst.equipement_inst !== undefined){
      this.aquaInstForEditForm.get('equipement_inst')?.setValue(this.editAquaInst.equipement_inst);
    }
  }

  public onUpdateAquaInst(): void{
    let retrievedData = this.aquaInstForEditForm.value;
    retrievedData['arron_id'] = this.editAquaInst.arron_id;
    retrievedData['position_id'] = this.editAquaInst.position?.id;
    this._aquaService.editAquaInst(retrievedData, this.editAquaInst.id).subscribe(
      (response: InstallationAquatique) => {
        this._sharedService.aquaInstallation = response;
        this.modal.close('Ok click');
        this._notifierService.showSuccessMessage('', `Modification de ${response.nom_installation} a reussit!`, 'success');
        this.success = true;

      },
      (error: HttpErrorResponse) => {
        console.log('error . error[errors] :', error.error['errors'])
        this.errorMessage= error.error.message;
        this.errorMessages = error.error['errors']
        console.log('error status:', error.status);
        console.log('error message :', error.message);
        console.log('error statusText :',error.statusText)
      }
    );
  }
}
