import { DatePipe } from '@angular/common';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DeletionComponent } from './components/deletion/deletion.component';
import { EditGlissadeComponent } from './components/edit-glissade/edit-glissade.component';
import { EditAquaComponent } from './components/edit-aqua/edit-aqua.component';
import { EditPatinoireComponent } from './components/edit-patinoire/edit-patinoire.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DeletionComponent,
    EditGlissadeComponent,
    EditAquaComponent,
    EditPatinoireComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule
  ],

  providers: [DatePipe],
  bootstrap: [AppComponent],
  entryComponents: [DeletionComponent]

})
export class AppModule { }
