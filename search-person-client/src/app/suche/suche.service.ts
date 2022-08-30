import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { PersonDTO } from '../person.dto';
import { AlgoCompareDTO } from '../algo-compare.dto';


@Injectable({
    providedIn: 'root'
})
export class SucheService {

    constructor(private httpClient: HttpClient) {
    }

    searchResults$: Observable<PersonDTO[]> = new BehaviorSubject<PersonDTO[]>([]);

    // tslint:disable-next-line:max-line-length
    findMatches(name: string, firstname: string, algoType: string, nameThreshold: number, firstnameThreshold: number, wordSimilarity: boolean, wordSimilarityNameThreshold: number, wordSimilarityFirstnameThreshold: number): Observable<PersonDTO[]> {
        return this.httpClient.get<PersonDTO[]>(`http://localhost:5000/search?name=${name}&firstname=${firstname}&algoType=${algoType}&nameThreshold=${nameThreshold}&firstnameThreshold=${firstnameThreshold}&wordSimilarity=${wordSimilarity}&wordSimilarityNameThreshold=${wordSimilarityNameThreshold}&wordSimilarityFirstnameThreshold=${wordSimilarityFirstnameThreshold}`);
    }


    findAll(): Observable<PersonDTO[]> {
        return this.httpClient.get<PersonDTO[]>(`http://localhost:5000/persons`);
    }

    test(str1: string, str2: string, ignoreCase: boolean, ignoreAccent: boolean): Observable<AlgoCompareDTO[]> {
        return this.httpClient.get<AlgoCompareDTO[]>(`http://localhost:5000/test?str1=${str1}&str2=${str2}&ignoreCase=${ignoreCase}&ignoreAccent=${ignoreAccent}`);
    }
}
