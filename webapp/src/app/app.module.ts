import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AlumnoDetailComponent } from './features/alumnos/alumno-detail/alumno-detail.component';
import { AlumnosListComponent } from './features/alumnos/alumnos-list/alumnos-list.component';
import { NotFoundPageComponent } from './pages/not-found-page/not-found-page.component';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import { AppRoutingModule } from './app-routing.module';

import { HttpClientModule } from '@angular/common/http';
import { AlumnosServiceService } from './features/alumnos/alumnos-service.service';
import { AuthService } from './services/auth.service';


@NgModule({
  declarations: [
    AppComponent,
    AlumnoDetailComponent,
    AlumnosListComponent,
    NotFoundPageComponent,
    FooterComponent,
    HeaderComponent,
    LoginFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    AlumnosServiceService,
    AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
