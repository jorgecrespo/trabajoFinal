import { Component, OnInit } from '@angular/core';
import { AlumnosServiceService } from '../alumnos-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Alumno } from '../clases/alumno';
import { Nota } from '../clases/notas';

@Component({
  selector: 'app-alumno-detail',
  templateUrl: './alumno-detail.component.html',
  styleUrls: ['./alumno-detail.component.scss']
})
export class AlumnoDetailComponent implements OnInit {

  constructor(
    public alumnosService: AlumnosServiceService,
    private activatedRoute: ActivatedRoute,
    private router: Router
  ) { }

  alumno : Alumno;
  notas: Nota[]= [];

  ngOnInit() {

    const id = this.activatedRoute.snapshot.paramMap.get('id');

    this.cargarAlumno(id);

    this.cargarNotas(id);

   
  }

  cargarAlumno(id){
    this.alumnosService.getAlumnoPorId( id ).then( alumno => {

      if ( !alumno ) {
        return this.router.navigateByUrl('/')
      }
      this.alumno = alumno
      console.log( alumno )
    })    
  }

  cargarNotas(alumno_id){

    this.alumnosService.getNotas( alumno_id ).then( notas =>{
      this.notas = notas;
      console.log(notas)
    })


  }



}
