import { InstallationAquatique, InstAquaForEdit } from 'src/app/models/installation-aquatique';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { environment } from 'src/environments/environment';
import { tap } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':'application/json',
  })
}

@Injectable({
  providedIn: 'root'
})
export class AquaInstService {
  private apiServerUrl = environment.apiBaseUrl;
  private _refreshNeeded$ = new Subject<void>();

  constructor(private httpClient: HttpClient) { }

  get refreshNeeded$(){
    return this._refreshNeeded$;
  }

  public editAquaInst(aquaInst: InstAquaForEdit, aqua_inst_id: number): Observable<InstallationAquatique> {
    console.log('Aqua Inst to be updated in aqua inst service :',aquaInst)
    const url = `${this.apiServerUrl}/api/installation_aquatique/${aqua_inst_id}`
    return this.httpClient.put<InstallationAquatique>(url, aquaInst, httpOptions)
    .pipe(
      tap(()=>{
        this._refreshNeeded$.next();
        console.log('Aqua inst  has been updated in aqua inst service');
       }),
    );
  }
}










