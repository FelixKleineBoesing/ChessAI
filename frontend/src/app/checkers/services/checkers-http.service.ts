import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable()
export class CheckersHttpService {

  constructor(private http: HttpClient) { }

  sendMove(start: { row: number, col: number }, end: { row: number, col: number }): Observable<any> {
    const params: HttpParams = new HttpParams().set('startRow', start.row.toString());
    params.append('startCol', start.col.toString());
    params.append('endCol', end.col.toString());
    params.append('endRow', end.row.toString());

    return this.http.get<any>(environment.url, { params });
  }
  
  getAvailablePlayers(): Observable<any> {

    const agents = this.http.get("http://localhost:5001/get-agents", {});
    console.log(agents);
    return agents;
  }

  runGame(agent_one: string, agent_two: string): Observable<any> {
    const params: HttpParams = new HttpParams().set('agent_one', agent_one);
    params.append("agent_two", agent_two);
    return this.http.get("http://localhost:5001/game-with-two-agents", { params });
  }

}
