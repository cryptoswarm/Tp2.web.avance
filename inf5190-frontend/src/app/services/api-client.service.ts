import { Patinoire } from './../models/patinoire';
import { InstallationAquatique } from './../models/installation-aquatique';
import { Installation } from './../models/installation';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { Glissade } from '../models/glissade';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':'application/json',
  })
}

@Injectable({
  providedIn: 'root'
})
export class ApiClientService {


  private apiServerUrl = environment.apiBaseUrl;
  constructor(private httpClient: HttpClient) { }

  public getInstallationsPerArrondissement(arron_name: string): Observable<Installation>{
    const url = `${this.apiServerUrl}/api/installations?arrondissement=${arron_name['search']}`
    return this.httpClient.get<Installation>(url, httpOptions)
  }

  public getAquaInstallationDetails(arronName:string, aquaInstName: string): Observable<InstallationAquatique[]>{
    console.log('arron_name :',arronName['search'])
    const url = `${this.apiServerUrl}/api/installations/arrondissement/${arronName['search']}/aquatique/${aquaInstName}`
    console.log('url: ',url)
    return this.httpClient.get<InstallationAquatique[]>(url, httpOptions)
  }

  public getPatinoireDetails(arron_name:string, patinoireName: string): Observable<Patinoire>{
    console.log('arron_name :',arron_name['search'])
    const url = `${this.apiServerUrl}/api/installations/arrondissement/${arron_name['search']}/patinoire/${patinoireName}`
    console.log('url: ',url)
    return this.httpClient.get<Patinoire>(url, httpOptions)
  }

  public getGlissadeDetails(arrName: string, glissadeName: string): Observable<Glissade> {
    console.log('arron_name :',arrName['search'])
    const url = `${this.apiServerUrl}/api/installations/arrondissement/${arrName['search']}/glissade/${glissadeName}`
    return this.httpClient.get<Glissade>(url, httpOptions);
  }
}
