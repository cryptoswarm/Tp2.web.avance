import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { DatePipe } from '@angular/common';
import { GlissadeForEdit } from './../../models/glissade';
import { Glissade } from 'src/app/models/glissade';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { GlissadeServiceService } from 'src/app/services/glissade-service.service';
import { HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import Swal, { SweetAlertIcon } from 'sweetalert2'

@Component({
  selector: 'app-edit-glissade',
  templateUrl: './edit-glissade.component.html',
  styleUrls: ['./edit-glissade.component.css']
})
export class EditGlissadeComponent implements OnInit {

  // @Output() updatedGlissadEvent = new EventEmitter<Glissade>();
  // // @Output() updatedGlissadEvent = new EventEmitter<boolean>();
  editGlissade!: Glissade;

  errorMessage: string = "";
  errorMessages: string[] = [];
  date_maj: string = '';
  deblayee: string = ''
  ouvert: string = '';
  success : boolean = false;

  glissadeForEditForm!: FormGroup;

  constructor(private _sharedService:SharedServiceService,
              private _glissadeService : GlissadeServiceService,
              private _datePipe: DatePipe,
              private _formBuilder: FormBuilder,
              public modal: NgbActiveModal) {}

  ngOnInit(): void {

    this.glissadeForEditForm = this._formBuilder.group({
      name: ['', Validators.required],
      date_maj: ['', Validators.required],
      ouvert: ['', [Validators.required,
                    Validators.pattern('(^Oui$)|(^Non$)'),
                    Validators.min(3),
                    Validators.max(3)]],
      deblaye: ['', [Validators.required,
                    Validators.pattern('(^Oui$)|(^Non$)'),
                    Validators.min(3),
                    Validators.max(3)]],
      condition: ['', Validators.required]
    })

    this.editGlissade = this._sharedService.glissade;
    if(this.editGlissade.name !== undefined){
        this.glissadeForEditForm.get('name')?.setValue(this.editGlissade.name);
    }
    if(this.editGlissade.date_maj !== undefined){
      let value = this._datePipe.transform(new Date(this.editGlissade.date_maj), 'yyyy-MM-ddTHH:mm')
      if(  value !== null){
        this.glissadeForEditForm.get('date_maj')?.setValue(value);
      }
    }
    if(this.editGlissade.deblaye !== undefined){
      let value = this.editGlissade.deblaye == true ? 'Oui': 'Non'
      if(  value !== null){
        this.glissadeForEditForm.get('deblaye')?.setValue(value);
      }
    }
    if(this.editGlissade.ouvert !== undefined){
      let value = this.editGlissade.ouvert == true ? 'Oui': 'Non'
      if(  value !== null){
        this.glissadeForEditForm.get('ouvert')?.setValue(value);
      }
    }
    if(this.editGlissade.condition !== undefined){
        this.glissadeForEditForm.get('condition')?.setValue(this.editGlissade.condition);
    }
  }

  public onUpdateGlissade(): void{
    let glissade = this.convertToGlissadeForEdit();
    this._glissadeService.editGlissade(glissade, this.editGlissade.glissade_id).subscribe(
      (response: Glissade) => {
        console.log("Glissade has been Updated to :",response);
        this._sharedService.glissade = response;
        console.log('Update successful :',this._sharedService.glissade);
        this.modal.close('Ok click');
        this.showSuccessMessage('', `Modification de ${response.name} a reussit!`, 'success');
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

  private convertToGlissadeForEdit(): GlissadeForEdit{
    const retrievedData = this.glissadeForEditForm.value;
    let glissade = new GlissadeForEdit();
    console.log('Data retrieved from form :',glissade)
    console.log('this.glissadeForEditForm.get(ouvert)?.value:',this.glissadeForEditForm.get('ouvert')?.value)
    console.log('retrievedData.ouvert !== undefined ;',retrievedData.ouvert !== undefined);
    if(retrievedData.date_maj !== undefined){
      glissade.date_maj = new Date(retrievedData.date_maj).toISOString();
    }
    glissade.arrondissement_id = this.editGlissade.arrondissement_id;
    if(retrievedData.condition){
      glissade.condition = retrievedData.condition;
    }
    if(retrievedData.deblaye){
      glissade.deblaye = retrievedData.deblaye == 'Oui' ? '1': '0';
    }
    if(retrievedData.ouvert){
      glissade.ouvert = retrievedData.ouvert == 'Oui' ? '1': '0';
    }
    glissade.name = retrievedData.name;
    console.log('glissade :',glissade);
    return glissade;
  }

  showSuccessMessage( title: string, message: string, icon: SweetAlertIcon){
    Swal.fire(
      'Good job!',
      message= message,
      icon = icon
    )
  }


}
