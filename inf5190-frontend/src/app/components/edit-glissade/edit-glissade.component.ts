import { DatePipe } from '@angular/common';
import { GlissadeForEdit } from './../../models/glissade';
import { Glissade } from 'src/app/models/glissade';
import { Component, Input, OnInit } from '@angular/core';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { GlissadeServiceService } from 'src/app/services/glissade-service.service';
import { HttpErrorResponse } from '@angular/common/http';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-edit-glissade',
  templateUrl: './edit-glissade.component.html',
  styleUrls: ['./edit-glissade.component.css']
})
export class EditGlissadeComponent implements OnInit {

  editGlissade!: Glissade;
  // glissade!: GlissadeForEdit;
  errorMessage: string = "";
  errorMessages: string[] = [];
  date_maj: string = '';
  deblayee: string = ''
  ouvert: string = '';

  glissadeForEditForm: FormGroup;

  constructor(private _sharedService:SharedServiceService,
              private _glissadeService : GlissadeServiceService,
              private _datePipe: DatePipe,
              private _formBuilder: FormBuilder) {

                this.glissadeForEditForm = this._formBuilder.group({
                  name: ['', Validators.required],
                  date_maj: ['', Validators.required],
                  ouvert: ['', Validators.required],
                  deblaye: ['', Validators.required],
                  condition: ['', Validators.required]
                })
               }

  ngOnInit(): void {
    this.editGlissade = this._sharedService.glissade;
    if(this.editGlissade.date_maj !== undefined){
      let value = this._datePipe.transform(new Date(this.editGlissade.date_maj), 'yyyy-MM-ddTHH:mm')
      if(  value !== null){
        this.date_maj = value;
      }
    }
    if(this.editGlissade.deblaye !== undefined){
      let value = this.editGlissade.deblaye == true ? 'Oui': 'Non'
      if(  value !== null){
        this.deblayee = value;
      }
    }
    if(this.editGlissade.ouvert !== undefined){
      let value = this.editGlissade.ouvert == true ? 'Oui': 'Non'
      if(  value !== null){
        this.ouvert = value;
      }
    }
  }

  public onUpdateGlissade(): void{
    const retrievedData = this.glissadeForEditForm.value;
    console.log('retrievedDataFromEditForm glissade edit form: ',retrievedData)
    // console.log('Glissade to be edited date before convert :',updatedGlissade.date_maj);
    // console.log('Before editglissade :', updatedGlissade);
    let glissade = this.convertToGlissadeForEdit(retrievedData);
    console.log('Glissade to be edited date after convert :',glissade.date_maj);
    this._glissadeService.editGlissade(glissade, this.editGlissade.glissade_id).subscribe(
      (response: Glissade) => {
        console.log("Glissade has been Updated to :",response);
        // this.getEmployees();
        this._sharedService.glissade = response;
        console.log('Update successful :',this._sharedService.glissade);
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

  private convertToGlissadeForEdit(updatedGlissade: Glissade): GlissadeForEdit{
    let glissade = new GlissadeForEdit();
    if(updatedGlissade.date_maj !== undefined){
      console.log('updatedGlissade.date_maj !== undefined :', updatedGlissade.date_maj !== undefined)
      console.log('updatedGlissade.date_maj :',updatedGlissade.date_maj)
      glissade.date_maj = new Date(updatedGlissade.date_maj).toISOString();
    }
    glissade.arrondissement_id = this.editGlissade.arrondissement_id;
    if(updatedGlissade.condition){
      glissade.condition = updatedGlissade.condition;
    }
    if(updatedGlissade.deblaye !== undefined){
      console.log('Value from form updatedGlissade.deblaye :',updatedGlissade.deblaye)
      console.log('glissade.deblaye before evaluating :',glissade.deblaye)
      console.log('updatedGlissade.deblaye == true',updatedGlissade.deblaye === true)
      console.log('typeof(updatedGlissade.deblaye)',typeof(updatedGlissade.deblaye))
      // glissade.deblaye = updatedGlissade.deblaye == 'Oui' ? '1': '0';
      console.log('After evaluating condition of deblaye :',glissade.deblaye)
    }
    if(updatedGlissade.ouvert !== undefined){
      console.log('Value from form updatedGlissade.ouvert :',updatedGlissade.ouvert)
      glissade.ouvert = updatedGlissade.ouvert == true ? '1': '0';
      console.log('After evaluating condition of ouvert :',glissade.ouvert)
    }
    glissade.name = updatedGlissade.name;
    console.log('updatedGlissade.name: ',glissade.name)
    return glissade;
  }
}
