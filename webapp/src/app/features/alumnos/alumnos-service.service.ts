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
    console.log("servicio alumnos funcionando")
   }


  getAlumnos(): Promise<Alumno[]> {
    
    if ( this.alumnos.length > 0 ){
      return Promise.resolve( this.alumnos );
    }

    return new Promise ( resolve => {

    this.http.get('http://localhost:8000/alumnos/')
      .subscribe( (alumnos: Alumno[]) => {

        console.log(alumnos)

        this.alumnos = alumnos;
        resolve( alumnos );

      });

    });
      
  }

  getAlumnoPorId( id: string){

    if ( this.alumnos.length > 0 ){

      const alumno = this.alumnos.find( alumno => alumno.id == id);
      return Promise.resolve(alumno); 
    } 

    return this.getAlumnos().then( alumnos => {

      const alumno = this.alumnos.find( alumno => {

         return alumno.id == id
      });
      return Promise.resolve( alumno )

    })



  }

  // ==========================
  // NOTAS
  // ==========================

  getNotas(alumno_id): Promise<Nota[]> {
    


    return new Promise ( resolve => {

    this.http.get('http://localhost:8000/notas/'+ alumno_id + '/')
      .subscribe( (notas: Nota[]) => {

        console.log(notas)

        this.notas = notas;
        resolve( notas );

      });

    });

  }
/*

  getNotaPorIdAlumno( alumno_id: string){

    if ( this.notas.length > 0 ){

      const notas = this.notas.find( nota => nota.alumno_id == alumno_id);
      return Promise.resolve(notas); 
    } 

    return this.getNotas().then( notas: Notas[] => {

      const notas: Nota[]] = this.alumnos.find( notas: any[] => {

         return notas.alumno_id == alumno_id
      });
      return Promise.resolve( alumno )

    })


*/
  }



}
