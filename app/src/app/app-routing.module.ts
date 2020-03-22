import { NgModule } from '@angular/core';
import { Routes, RouterModule, Route } from '@angular/router';
import { RegisterationComponent } from './components/registeration/registeration.component'
import { HomeComponent } from './components/home/home.component'


const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path : 'register', component: RegisterationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
