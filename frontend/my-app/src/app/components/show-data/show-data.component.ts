import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { CommonModule } from '@angular/common';
import { DataService } from '../../services/data-service.service';
@Component({
  selector: 'app-show-data',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './show-data.component.html',
  styleUrl: './show-data.component.css',
})
export class ShowDataComponent {
  data: any;
  private req: any;

  constructor(private service: DataService) {}

  ngOnInit() {
    this.req = this.service.getData().subscribe((data) => {
      console.log(JSON.stringify(data));
      this.data = data;
    });
  }

  ngOnDestroy() {
    this.req.unsubscribe();
  }
}
