import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../classes/user';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  apiURL: string = "https://127.0.0.1:8080"

  constructor(private httpClient: HttpClient) { }

  public createUser(user: User){
      console.log(user);
      var response = this.httpClient.post(this.apiURL + '/user', user);
      console.log(response);
      return response
  }

  public getUserByUname(uname: string){
    return this.httpClient.get(`${this.apiURL}/user/${uname}`)
  }

}
