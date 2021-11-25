import { Component, OnInit, Type } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Glissade } from 'src/app/models/glissade';
import { SharedServiceService } from 'src/app/services/shared-service.service';


@Component({
  selector: 'app-deletion',
  templateUrl: './deletion.component.html',
  styleUrls: ['./deletion.component.css']
})
export class DeletionComponent implements OnInit {

  deleteInstallationId!: number;

  constructor(public modal: NgbActiveModal,
              private _sharedService:SharedServiceService) {}

  ngOnInit(): void {
    this.deleteInstallationId = this._sharedService.installationId;
  }

  public onDeleteInstallation(): void{

  }

}
