import { GlissadeForEdit } from './../models/glissade';
import { Observable , Subject, throwError} from 'rxjs';
import { Glissade } from 'src/app/models/glissade';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { map , catchError, tap} from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':'application/json',
  })
}

@Injectable({
  providedIn: 'root'
})
export class GlissadeServiceService {

  private apiServerUrl = environment.apiBaseUrl;

  private _refreshNeeded$ = new Subject<void>();

  constructor(private httpClient: HttpClient) { }

  get refreshNeeded$(){
    return this._refreshNeeded$;
  }


  public editGlissade(glissade: GlissadeForEdit, glissade_id: number): Observable<Glissade> {
    // /api/glissade/<id>
    console.log('Glissade to be updated in glissade service :',glissade)
    const url = `${this.apiServerUrl}/api/glissade/${glissade_id}`
    return this.httpClient.put<Glissade>(url, glissade, httpOptions)
    .pipe(
      tap(()=>{
        this._refreshNeeded$.next();
        console.log('glissade  has been updated in glissade service');
       }),
    );
    // .pipe(map(response =>{
    //   return response;
    // }),
    //   catchError((err) => {
    //   console.log('error caught in service')
    //   console.error(err);

    //   //Handle the error here in the serive or Rethrow it back to component as below
    //   return throwError(err);
    //   })
    // );
  }

}
