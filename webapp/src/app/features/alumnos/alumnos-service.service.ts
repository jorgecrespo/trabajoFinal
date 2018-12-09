import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AlumnosServiceService {

  private alumnos: any;

  constructor( private http : HttpClient) {
    console.log("servicio alumnos funcionando")
   }


  getAlumnos(){
    
    return this.http.get('http://localhost:8000/alumnos/')
   
  }



}
