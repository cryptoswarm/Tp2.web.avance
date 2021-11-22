import { Glissade } from 'src/app/models/glissade';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedServiceService {

  constructor() { }

  private _glissadeEditData!: Glissade;

  get glissade() {
    return this._glissadeEditData;
  }

  set glissade(glissade: Glissade) {
    this._glissadeEditData = glissade;
  }
}
