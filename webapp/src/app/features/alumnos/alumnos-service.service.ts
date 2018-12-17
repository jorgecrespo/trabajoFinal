import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
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

  getNotas(alumno_id): Promise<Nota[]> {
    

/*
    return new Promise ( resolve => {

      this.http.get('http://localhost:8000/api/v1/notas/'+ alumno_id + '/')
        .subscribe( (notas: Nota[]) => {

         // console.log(notas)

          this.notas = notas;
          resolve( notas );

        });

    });
*/
  }

  



}
