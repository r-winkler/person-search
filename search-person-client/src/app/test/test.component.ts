import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { combineLatest, Observable, of } from 'rxjs';
import { SucheService } from '../suche/suche.service';
import { auditTime, catchError, shareReplay, startWith, switchMap } from 'rxjs/operators';
import { AlgoCompareDTO } from '../algo-compare.dto';

@Component({
    selector: 'app-test',
    templateUrl: './test.component.html',
    styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {

    testForm: FormGroup;
    string1Control: AbstractControl | null;
    string2Control: AbstractControl | null;
    ignoreCaseControl: AbstractControl | null;
    ignoreAccentControl: AbstractControl | null;

    algoCompare$: Observable<AlgoCompareDTO>;


    constructor(private fb: FormBuilder,
                private sucheService: SucheService) {

        this.testForm = this.fb.group({
            string1: ['', [Validators.required]],
            string2: ['', [Validators.required]],
            ignoreCase: [''],
            ignoreAccent: ['']
        });

        this.string1Control = this.testForm.get('string1');
        this.string2Control = this.testForm.get('string2');
        this.ignoreCaseControl = this.testForm.get('ignoreCase');
        this.ignoreAccentControl = this.testForm.get('ignoreAccent');

        // @ts-ignore
        this.algoCompare$ = combineLatest([
            this.string1Control?.valueChanges.pipe(auditTime(300)),
            this.string2Control?.valueChanges.pipe(auditTime(300)),
            this.ignoreCaseControl?.valueChanges.pipe(startWith(false)),
            this.ignoreAccentControl?.valueChanges.pipe(startWith(false))
        ]).pipe(
            switchMap(() => this.sucheService.test(this.string1Control?.value, this.string2Control?.value, this.ignoreCaseControl?.value, this.ignoreAccentControl?.value)
                .pipe(
                    catchError(_ => of([]))
                )
            ),
            shareReplay(1)
        );

    }

    ngOnInit(): void {

        this.algoCompare$.subscribe((val) => console.log(val));
    }

}
