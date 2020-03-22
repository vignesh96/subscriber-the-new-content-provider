import { NgModule } from '@angular/core';
import { Routes, RouterModule, Route } from '@angular/router';
import { RegisterationComponent } from './components/registeration/registeration.component'


const routes: Routes = [
  { path : 'register', component: RegisterationComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
