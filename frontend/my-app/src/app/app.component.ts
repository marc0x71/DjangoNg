import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ShowDataComponent } from './components/show-data/show-data.component';
import { DataService } from './services/data-service.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    ShowDataComponent,
    HttpClientModule
  ],
  providers: [DataService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my-app';
}
