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
    const retrievedData = this.glissadeForEditForm.value;
    let glissade = this.convertToGlissadeForEdit(retrievedData);
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

  private convertToGlissadeForEdit(updatedGlissade: any): GlissadeForEdit{
    let glissade = new GlissadeForEdit();
    if(updatedGlissade.date_maj !== undefined){
      glissade.date_maj = new Date(updatedGlissade.date_maj).toISOString();
    }
    glissade.arrondissement_id = this.editGlissade.arrondissement_id;
    if(updatedGlissade.condition){
      glissade.condition = updatedGlissade.condition;
    }
    if(updatedGlissade.deblaye !== undefined){
      glissade.deblaye = updatedGlissade.deblaye == 'Oui' ? '1': '0';
    }
    if(updatedGlissade.ouvert !== undefined){
      glissade.ouvert = updatedGlissade.ouvert == 'Oui' ? '1': '0';
    }
    glissade.name = updatedGlissade.name;
    return glissade;
  }
}
