import { Installation } from './../models/installation';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

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

  public getInstallationsPerArrondissement(arron_name: string): Observable<Installation[]>{
    return this.httpClient.get<Installation[]>(`${this.apiServerUrl}/api/installations?arrondissement=${arron_name['search']}`, httpOptions)
  }
}
