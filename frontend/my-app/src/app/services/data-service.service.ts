import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private baseUrl = 'http://localhost:8000'
  constructor(private httpClient: HttpClient) {}

  getData() {
    return this.httpClient.get<any>(this.baseUrl+'/getData');
  }
}
