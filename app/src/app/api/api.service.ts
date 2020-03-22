import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../classes/user';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  apiURL: string = "https://localhost:8080"

  constructor(private httpClient: HttpClient) { }

  public createUser(user: User){
      return this.httpClient.post(`${this.apiURL}/user`, user);
  }

  public getUserByUname(uname: string){
    return this.httpClient.get(`${this.apiURL}/user/${uname}`)
  }

}
