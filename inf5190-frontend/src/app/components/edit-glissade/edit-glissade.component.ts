import { Glissade } from 'src/app/models/glissade';
import { Component, Input, OnInit } from '@angular/core';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { GlissadeServiceService } from 'src/app/services/glissade-service.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-edit-glissade',
  templateUrl: './edit-glissade.component.html',
  styleUrls: ['./edit-glissade.component.css']
})
export class EditGlissadeComponent implements OnInit {

  editGlissade!: Glissade;
  errorMessage: string = "";
  errorMessages: string[] = [];

  constructor(private _sharedService:SharedServiceService,
              private _glissadeService : GlissadeServiceService) { }

  ngOnInit(): void {
    this.editGlissade = this._sharedService.glissade;
  }

  public onUpdateGlissade(): void{

    this._glissadeService.editGlissade(this.editGlissade).subscribe(
      (response: Glissade) => {
        console.log("Updating glissade :",response);
        // this.getEmployees();
        this._sharedService.glissade = response;
      },
      (error: HttpErrorResponse) => {
        console.log('error . error[errors] :', error.error['errors'])
        this.errorMessage= error.error.message;
        this.errorMessages = error.error['errors']
        console.log('error status:', error.status);
        console.log('error message :', error.message);
        console.log('error statusText :',error.statusText)
        // alert(error.message);
      }
    );
  }

}
