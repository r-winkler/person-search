import { Component, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';
import { SucheService } from '../suche/suche.service';
import { first, map } from 'rxjs/operators';
import { PersonDTO } from '../person.dto';

@Component({
  selector: 'app-suchresultate',
  templateUrl: './suchresultate.component.html',
  styleUrls: ['./suchresultate.component.scss']
})
export class SuchresultateComponent implements OnInit {

  displayedColumns: string[] = ['name', 'firstname'];
  first100Results$: Observable<PersonDTO[]>;

  constructor(public sucheService: SucheService) {

    this.first100Results$ = this.sucheService.searchResults$.pipe(map(res => res.slice(0, 100)));
  }

  ngOnInit(): void {


  }

}
