import { Injectable } from '@angular/core';
import Swal, { SweetAlertIcon } from 'sweetalert2';

@Injectable({
  providedIn: 'root'
})
export class NotifierService {

  constructor() { }

  public showSuccessMessage( title: string, message: string, icon: SweetAlertIcon){
    Swal.fire(
      'Good job!',
      message= message,
      icon = icon
    )
  }
}
