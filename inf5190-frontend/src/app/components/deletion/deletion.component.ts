import { HttpErrorResponse } from '@angular/common/http';
import { AquaInstService } from 'src/app/services/aqua-inst.service';
import { GlissadeServiceService } from 'src/app/services/glissade-service.service';
import { Component, OnInit, Type } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Glissade } from 'src/app/models/glissade';
import { SharedServiceService } from 'src/app/services/shared-service.service';
import { NotifierService } from 'src/app/services/notifier.service';


@Component({
  selector: 'app-deletion',
  templateUrl: './deletion.component.html',
  styleUrls: ['./deletion.component.css']
})
export class DeletionComponent implements OnInit {

  deleteInstallationId!: number;
  installationType!: string;
  errorMessage: string = ''
  errorMessages: string[] = [];
  success : boolean = false;
  installationName: string ='';

  constructor(public modal: NgbActiveModal,
              private _sharedService:SharedServiceService,
              private _glissadeService: GlissadeServiceService,
              private _aquaService: AquaInstService,
              private _notifierService:NotifierService) {}

  ngOnInit(): void {
    this.deleteInstallationId = this._sharedService.installationId;
    this.installationType = this._sharedService.installationType;
    this.installationName = this._sharedService.installationName;
  }

  public onDeleteInstallation(): void{
    this.success = false;
    if(this.installationType == 'glissade'){
      this._aquaService.deleteAquaInst(this.deleteInstallationId, 'glissade').subscribe((response)=>{
        this._notifierService.showSuccessMessage('', `Suppression de ${response.nom_installation} a reussit!`, 'success');
        this.success = true;
        this.modal.close()
        // (click)="modal.close('Ok click')"
      },
      (error: HttpErrorResponse)=>{
        console.log('error . error[errors] :', error.error['errors'])
        this.errorMessage= error.error.message;
        this.errorMessages = error.error['errors']
        console.log('error status:', error.status);
        console.log('error message :', error.message);
        console.log('error statusText :',error.statusText)
      })
    }else if(this.installationType == 'installation_aquatique'){

    }else if(this.installationType == 'patinoire-condition'){
    }
  }

}
