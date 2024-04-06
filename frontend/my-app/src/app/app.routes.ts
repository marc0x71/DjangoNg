import { Routes } from '@angular/router';
import { ShowDataComponent } from './components/show-data/show-data.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';

export const routes: Routes = [
  {
    path:"",
    component: ShowDataComponent,
},
{
    path:"**",
    component: PageNotFoundComponent,
}
];
