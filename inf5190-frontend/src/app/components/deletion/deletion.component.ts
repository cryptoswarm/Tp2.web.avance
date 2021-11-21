import { Component, OnInit, Type } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';


@Component({
  selector: 'app-deletion',
  templateUrl: './deletion.component.html',
  styleUrls: ['./deletion.component.css']
})
export class DeletionComponent implements OnInit {


  constructor(public modal: NgbActiveModal) {}

  ngOnInit(): void {
  }

}
