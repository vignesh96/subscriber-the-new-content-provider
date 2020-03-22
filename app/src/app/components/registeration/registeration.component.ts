import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api/api.service';
import { User } from '../../classes/user';

@Component({
  selector: 'app-registeration',
  templateUrl: './registeration.component.html',
  styleUrls: ['./registeration.component.css']
})
export class RegisterationComponent implements OnInit {

  constructor(private apiService: ApiService) { }
  
  ngOnInit(): void {
  }

  createUser(user: User){
    console.log("User data" + JSON.stringify(user));
    console.log("Uname data" + user.uname);
    this.apiService.createUser(user).subscribe((res) => {
      console.log("Creating a customer!");
    })
  }

}
