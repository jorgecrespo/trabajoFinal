import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  autenticado : boolean = false;

  constructor() { }
}
