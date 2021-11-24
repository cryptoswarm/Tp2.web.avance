import { Patinoire } from 'src/app/models/patinoire';
import { InstallationAquatique } from 'src/app/models/installation-aquatique';
import { Glissade } from 'src/app/models/glissade';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedServiceService {

  constructor() { }

  private _glissadeEditData!: Glissade;
  private _aquaInstallationData!: InstallationAquatique;
  private _patinoireData!: Patinoire;

  get glissade() {
    return this._glissadeEditData;
  }

  set glissade(glissade: Glissade) {
    this._glissadeEditData = glissade;
  }

  get aquaInstallation(){
    return this._aquaInstallationData;
  }

  set aquaInstallation(aqua: InstallationAquatique) {
    this._aquaInstallationData = aqua;
  }

  get patinoire(){
    return this._patinoireData;
  }

  set patinoire(patinoire: Patinoire) {
    this._patinoireData = patinoire;
  }
}
