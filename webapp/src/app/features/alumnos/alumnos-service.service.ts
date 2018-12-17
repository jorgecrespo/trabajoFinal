import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Alumno } from './clases/alumno';
import { Nota } from './clases/notas';

@Injectable({
  providedIn: 'root'
})
export class AlumnosServiceService {

  private alumnos: Alumno[] = [];
  private notas: Nota[] = [];

  constructor( private http : HttpClient) {
   // console.log("servicio alumnos funcionando")
  }





  getAlumnos() {    

    return this.http.get<Alumno>('http://localhost:8000/api/v1/alumnos/')     
      
  }



  getAlumnoPorId( id: string){
    
    return this.http.get<Alumno>('http://localhost:8000/api/v1/alumnos/'+ id + '/') 

  }

  // ==========================
  // NOTAS
  // ==========================

  getNotas(alumno_id ="1"){
    
    let params = new HttpParams();

    params = params.append('alumno', alumno_id )


    return this.http.get<Nota[]>('http://localhost:8000/api/v1/notas/', {params})

  }

  



}
