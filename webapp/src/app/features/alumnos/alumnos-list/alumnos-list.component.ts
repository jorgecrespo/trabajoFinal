import { Component, OnInit } from '@angular/core';
import { AlumnosServiceService } from '../alumnos-service.service';
import 'rxjs';

@Component({
  selector: 'app-alumnos-list',
  templateUrl: './alumnos-list.component.html',
  styleUrls: ['./alumnos-list.component.scss']
})
export class AlumnosListComponent implements OnInit {

  private alumnos : any;

  constructor(private alumnosService: AlumnosServiceService) { }


  ngOnInit() {
    
    
    this.alumnosService.getAlumnos()
      .subscribe( (data:any) =>{
        console.log("data: ", data)
        this.alumnos = data;
      })  
      
    
  }
}
