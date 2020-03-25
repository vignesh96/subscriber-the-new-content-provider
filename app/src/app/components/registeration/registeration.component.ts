import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api/api.service';
import { User } from '../../classes/user';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-registeration',
  templateUrl: './registeration.component.html',
  styleUrls: ['./registeration.component.css']
})
export class RegisterationComponent implements OnInit {

  register: FormGroup;
  constructor(private apiService: ApiService) { 
    this.register = new FormGroup({
      uname: new FormControl(),
      fname: new FormControl(),
      lname: new FormControl(),
      email: new FormControl(),
      dob: new FormControl(),
      password: new FormControl()
    })
    
  }
  
  ngOnInit(): void {
  }

  createUser(){

    var user = {
      "uname": this.register.value.uname,
      "fname": this.register.value.fname,
      "lname": this.register.value.lname,
      "email": this.register.value.email,
      "dob": this.register.value.dob,
      "password": this.register.value.password
    }

    console.log("User data" + JSON.stringify(user));
    this.apiService.createUser(user).subscribe((res) => {
      console.log("Creating a customer!");
    })
  }

}
