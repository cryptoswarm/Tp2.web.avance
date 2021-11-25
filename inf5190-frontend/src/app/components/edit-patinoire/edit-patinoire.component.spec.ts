import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditPatinoireComponent } from './edit-patinoire.component';

describe('EditPatinoireComponent', () => {
  let component: EditPatinoireComponent;
  let fixture: ComponentFixture<EditPatinoireComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditPatinoireComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditPatinoireComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
