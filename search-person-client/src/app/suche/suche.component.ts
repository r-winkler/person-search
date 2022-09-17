import { Component, OnInit } from '@angular/core';
import { AbstractControl, UntypedFormBuilder, UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';
import { BehaviorSubject, of, Subject } from 'rxjs';

import { catchError, exhaustMap, filter, finalize, shareReplay, tap } from 'rxjs/operators';
import { SucheService } from './suche.service';

@Component({
    selector: 'app-suche',
    templateUrl: './suche.component.html',
    styleUrls: ['./suche.component.scss']
})
export class SucheComponent implements OnInit {

    searchForm: UntypedFormGroup;
    nameControl: AbstractControl | null;
    firstnameControl: AbstractControl | null;
    algoTypeControl: UntypedFormControl;
    nameThresholdControl: UntypedFormControl;
    firstnameThresholdControl: UntypedFormControl;
    wordSimilarityControl: UntypedFormControl;
    wordSimilarityNameThresholdControl: UntypedFormControl;
    wordSimilarityFirstnameThresholdControl: UntypedFormControl;

    searchClick$ = new Subject();
    searching$ = new BehaviorSubject<boolean>(false);


    constructor(private fb: UntypedFormBuilder,
                private sucheService: SucheService) {

        this.searchForm = this.fb.group({
            name: ['', [Validators.required]],
            firstname: ['', [Validators.required]],
            algoType: ['jaro-winkler', [Validators.required]],
            nameThreshold: [65, [Validators.required]],
            firstnameThreshold: [65, [Validators.required]],
            wordSimilarity: [false, [Validators.required]],
            wordSimilarityNameThreshold: [30, [Validators.required]],
            wordSimilarityFirstnameThreshold: [30, [Validators.required]]
        });

        this.nameControl = this.searchForm.get('name');
        this.firstnameControl = this.searchForm.get('firstname');
        // @ts-ignore
        this.algoTypeControl = this.searchForm.get('algoType');
        // @ts-ignore
        this.nameThresholdControl = this.searchForm.get('nameThreshold');
        // @ts-ignore
        this.firstnameThresholdControl = this.searchForm.get('firstnameThreshold');
        // @ts-ignore
        this.wordSimilarityControl = this.searchForm.get('wordSimilarity');
        // @ts-ignore
        this.wordSimilarityNameThresholdControl = this.searchForm.get('wordSimilarityNameThreshold');
        // @ts-ignore
        this.wordSimilarityFirstnameThresholdControl = this.searchForm.get('wordSimilarityFirstnameThreshold');

        this.sucheService.searchResults$ = this.searchClick$.pipe(
            filter(() => this.searchForm.valid),
            tap(() => this.searching$.next(true)),
            exhaustMap(() => this.sucheService.findMatches(
                this.nameControl?.value,
                this.firstnameControl?.value,
                this.algoTypeControl?.value,
                this.nameThresholdControl?.value / 100,
                this.firstnameThresholdControl?.value / 100,
                this.wordSimilarityControl?.value,
                this.wordSimilarityNameThresholdControl?.value / 100,
                this.wordSimilarityFirstnameThresholdControl?.value / 100)
                .pipe(
                    catchError(_ => of([]))
                )
            ),
            tap(() => this.searching$.next(false)),
            shareReplay(1),
            finalize(() => this.searching$.next(false))
        );

    }

    ngOnInit(): void {

        this.sucheService.searchResults$.subscribe((val) => console.log(val));
    }

}
