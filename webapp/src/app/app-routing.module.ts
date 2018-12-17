import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AlumnosListComponent } from './features/alumnos/alumnos-list/alumnos-list.component';
import { AlumnoDetailComponent } from './features/alumnos/alumno-detail/alumno-detail.component';
import { NotFoundPageComponent } from './pages/not-found-page/not-found-page.component';



const routes: Routes =[
  { path: 'alumnos', component: AlumnosListComponent},
  { path: 'alumno/:id', component: AlumnoDetailComponent},
  { path: '**', component: NotFoundPageComponent}
]

@NgModule({
  imports: [
    RouterModule.forRoot( routes )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
